from mattermostdriver import Driver

class MattermostImport:
    @staticmethod
    def _getToken() -> str:
        token = input("Feed me with a personal token: ")

        if token == "":
            print("No token provided")
            exit(1)

        return token

    @staticmethod
    def _getHost() -> str:
        name = input("Feed me with the Mattermost instance hostname: ")

        if name == "":
            print("No hostname provided")
            exit(2)

        return name

    def upload(src: str) -> None:
        driver = Driver({
            'scheme': 'https',
            'url': MattermostImport._getHost(),
            'token': MattermostImport._getToken(),
            'port': 443,
        })

        driver.login()
        print(driver.emoji.get_custom_emoji_by_name("doge"))


if __name__ == "__main__":
    MattermostImport.upload("output")
