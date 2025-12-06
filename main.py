from reactome_service import ReactomeService


def progress(msg):
    print(msg)


def main():
    print("\n=== Reactome Pathway Downloader ===\n")

    email = input("Enter your contact email: ").strip()
    st_id = input("Enter Reactome pathway ID (e.g., R-HSA-199420): ").strip()

    service = ReactomeService(email)

    service.download_all(st_id, progress_callback=progress)


if __name__ == "__main__":
    main()