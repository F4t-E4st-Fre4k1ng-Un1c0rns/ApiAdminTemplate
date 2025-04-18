from email.message import EmailMessage

from smtplibaio import SMTP_SSL

from src.settings import settings


class Client:
    """
    Для Gmail:
    1. В настройках аккаунта добавить двухфакторную аутентификацию
    2. Создать приложение, назвать его как угоодно. https://myaccount.google.com/apppasswords?utm_source=google-account&utm_medium=web
    3. Получить пароль от gmail
    4. Вставить этот пароль в .env
    """

    def __init__(
        self,
        host: str = settings.MAIL_HOST,
        port: int = settings.MAIL_PORT,
        login: str = settings.MAIL_LOGIN,
        password: str = settings.MAIL_PASSWORD,
    ):
        self._host = host
        self._port = port
        self._login = login
        self._password = password

    async def __aenter__(self):
        self._server = SMTP_SSL(self._host, self._port)
        await self._server.connect()
        await self._server.auth(self._login, self._password)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._server.quit()

    async def send_message(
        self, recipient_adresses: list[str], subject: str, html_content: str
    ) -> None:
        msg = EmailMessage()
        msg["From"] = self._login
        msg["To"] = ", ".join(recipient_adresses)
        msg["Subject"] = subject
        msg.set_content(html_content, "html")

        await self._server.sendmail(self._login, recipient_adresses, msg.as_string())
