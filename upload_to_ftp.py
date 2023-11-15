# from ftplib import FTP

# def upload_folder_to_ftp(ftp, local_folder_path, remote_folder_path):
#     try:
#         ftp.cwd(remote_folder_path)  
#         for item in os.listdir(local_folder_path):
#             local_item = os.path.join(local_folder_path, item)
#             if os.path.isfile(local_item):
#                 with open(local_item, 'rb') as file:
#                     ftp.storbinary(f'STOR {item}', file)
#             elif os.path.isdir(local_item):
#                 try:
#                     ftp.mkd(item)
#                 except Exception as e:
#                     print(f"Directory '{item}' already exists on the server.")
#                 upload_folder_to_ftp(ftp, local_item, item) 
#     except Exception as e:
#         print(f"An error occurred: {str(e)}")

# if __name__ == '__main__':
#     import os

#     # FTP server connection details
#     ftp_host = 'ftp.dbuglab.com'
#     ftp_user = 'dbug@dbuglab.com'
#     ftp_pass = '2jJwVLcrcebp'

#     local_folder_path = 'C:\\Users\\my-pc\\Desktop\\Nouman-python'


#     remote_folder_path = '/public_html/developer.dbuglab.com/AK/AP/Nouman-python'

   
#     try:
#         ftp = FTP(ftp_host)
#         ftp.login(ftp_user, ftp_pass)
#         print(f"Connected to {ftp_host}")

       
#         upload_folder_to_ftp(ftp, local_folder_path, remote_folder_path)

        
#         ftp.quit()
#         print("FTP connection closed")
#     except Exception as e:
#         print(f"FTP connection failed: {str(e)}")
