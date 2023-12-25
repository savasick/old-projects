import flet as ft
import yt_dlp as yt

ydl_opts = {'format': 'bestvideo[ext=mp4]+bestaudio[ext=mp4]/mp4+best[height<=480]'}


def valid_link(link):
    extractors = yt.extractor.gen_extractors()
    for e in extractors:
        if e.suitable(link) and e.IE_NAME != 'generic':
            return True
    return False

def main(page: ft.Page):
    page.title = "DownTube"
    page.window_width = 600
    page.window_height = 200
    page.window_resizable = True
    page.update()

    def textbox_changed(e):
        url = e.control.value
        valid = valid_link(url)
        if valid:
            page.clean()
            
            with yt.YoutubeDL(ydl_opts) as ydl: 
                ydl.download([url])
            page.add(ft.Text("Done", size=30, color="green", text_align="center"))
            ytlink.value = ''
            page.add(ytlink)
        else:
            ytlink.error_text = "Not valuable youtube link"
            page.update()

    ytlink = ft.TextField(
        label="Add YouTube link",
        on_change=textbox_changed,
        text_align="center"
    )

    page.add(ytlink)

if __name__ == "__main__":
    ft.app(target=main)