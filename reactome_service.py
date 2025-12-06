import requests
from pathlib import Path


class ReactomeService:
    BASE_URL = "https://reactome.org/ContentService"

    def __init__(self, email: str, download_base=None):
        self.email = email
        self.download_folder = (
            Path(download_base)
            if download_base
            else Path.home() / "Desktop" / "Reactome_Downloads"
        )
        self.download_folder.mkdir(parents=True, exist_ok=True)

    # ---------------------------
    # INTERNAL UTILITIES
    # ---------------------------

    def _headers(self):
        return {"User-Agent": f"ReactomeDownloader/1.0 ({self.email})"}

    def _make_subfolder(self, st_id: str, sub: str):
        folder = self.download_folder / st_id / sub
        folder.mkdir(parents=True, exist_ok=True)
        return folder

    # ---------------------------
    # DOWNLOAD JSON
    # ---------------------------

    def download_json(self, st_id, progress_callback=None):
        url = f"{self.BASE_URL}/data/query/{st_id}"
        resp = requests.get(url, headers=self._headers())

        if resp.status_code != 200:
            if progress_callback:
                progress_callback(f"[ERROR] JSON {st_id}: HTTP {resp.status_code}")
            return None

        folder = self._make_subfolder(st_id, "json")
        path = folder / f"{st_id}.json"

        with open(path, "w", encoding="utf-8") as f:
            f.write(resp.text)

        if progress_callback:
            progress_callback(f"Saved JSON → {path}")

        return path

    # ---------------------------
    # DOWNLOAD PDF
    # ---------------------------

    def download_pdf(self, st_id, progress_callback=None):
        url = f"{self.BASE_URL}/exporter/document/event/{st_id}.pdf"
        resp = requests.get(url, headers=self._headers())

        if resp.status_code != 200:
            if progress_callback:
                progress_callback(f"[ERROR] PDF {st_id}: HTTP {resp.status_code}")
            return None

        folder = self._make_subfolder(st_id, "pdf")
        path = folder / f"{st_id}.pdf"

        with open(path, "wb") as f:
            f.write(resp.content)

        if progress_callback:
            progress_callback(f"Saved PDF → {path}")

        return path

    # ---------------------------
    # DOWNLOAD PNG
    # ---------------------------

    def download_png(self, st_id, progress_callback=None):
        url = f"{self.BASE_URL}/exporter/diagram/{st_id}.png"
        resp = requests.get(url, headers=self._headers())

        if resp.status_code != 200:
            if progress_callback:
                progress_callback(f"[ERROR] PNG {st_id}: HTTP {resp.status_code}")
            return None

        folder = self._make_subfolder(st_id, "png")
        path = folder / f"{st_id}.png"

        with open(path, "wb") as f:
            f.write(resp.content)

        if progress_callback:
            progress_callback(f"Saved PNG → {path}")

        return path

    # ---------------------------
    # MAIN METHOD: DOWNLOAD ALL
    # ---------------------------

    def download_all(self, st_id, progress_callback=None):
        if progress_callback:
            progress_callback(f"=== Downloading assets for {st_id} ===")

        self.download_json(st_id, progress_callback)
        self.download_pdf(st_id, progress_callback)
        self.download_png(st_id, progress_callback)

        if progress_callback:
            progress_callback(f"=== Completed downloads for {st_id} ===")