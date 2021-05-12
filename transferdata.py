import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
 
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
 
        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)
 
def main():
    access_token = 'c2ZmqO1cunYAAAAAAAAAAQrSdJNBcneZe8-TgQkXr0R_uynjaou-XaONPNarqC_z'
    transferData = TransferData(access_token)
 
    file_from = 'file1.txt' # This is name of the file to be uploaded
    file_to = 'https://www.dropbox.com/sh/hni3h5r10px15ar/AAAJ7vsDKXSNwt7iZy9FDXzla'  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.
 
    # API v2
    transferData.upload_file(file_from, file_to)
 
if __name__ == '__main__':
    main()