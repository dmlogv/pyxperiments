"""Try to read Windows clipboard text"""

import ctypes


CF_TEXT = 1

KERNEL32 = ctypes.windll.kernel32
USER32 = ctypes.windll.user32


def get_clipboard_text():
    """Get Windows clipboard text using WinAPI functions"""
    USER32.OpenClipboard(0)

    text = None

    if USER32.IsClipboardFormatAvailable(CF_TEXT):
        data = USER32.GetClipboardData(CF_TEXT)
        data_locked = KERNEL32.GlobalLock(data)
        text = ctypes.c_char_p(data_locked).value
        KERNEL32.GlobalUnlock(data_locked)
        return text

    USER32.CloseClipboard()

    if not text:
        raise Exception('No text in clipboard')

    return text


if __name__ == '__main__':
    print(get_clipboard_text())
