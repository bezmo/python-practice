import asyncio

from pyppeteer import launch


async def main():
    # ブラウザ起動
    browser = await launch(headless=False)

    # タブを開く
    page = await browser.newPage()

    # URLのページを開く
    asyncio.gather(
        page.goto('https://www.yahoo.co.jp/'),  # URLのページを開く
        page.waitForNavigation()                # ページの遷移を待つ
    )


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
