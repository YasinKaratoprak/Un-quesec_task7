import os
import time
def write_file():
    note = input("Dosyaya yazmak istediğin yazıyı gir Lütfen: ")

    with open('normal.txt', 'a') as dosya:
        dosya.write(f'\n {note} ')
def read_file():
    os.system("ls -la")
    readfile = input("okumak istediğin dosya adını gir:")
    try:
        with open(readfile, 'r') as dosya:

            content = dosya.read()
            print(f'{readfile} dosyasının içeriği:\n{content}')
    except FileNotFoundError:
        print(f'{readfile} dosyası bulunamadı.')
    except Exception as e:
        print(f'Hata oluştu: {e}')
def fileops(filename, operation):
    if operation == "create":
        try:
            with open(filename, 'w'):
                pass  # Dosyayı oluştur
            return f"{filename} adlı dosya oluşturuldu."
        except Exception as e:
            return f"Hata oluştu: {e}"

    elif operation == "del":
        os.system("sudo su")
        try:
            os.remove(filename)
            return f"{filename} adlı dosya silindi."
        except FileNotFoundError:
            return f"{filename} adlı dosya bulunamadı."
        except Exception as e:
            return f"Hata oluştu: {e}"

    else:
        return "Geçersiz işlem türü. 'create' veya 'del' kullanın."

write_file()
read_file()
fileops(filename="UNIQUESEC", operation="create")
print("DOSYA OLUŞTURULDU")
os.system("ls -la")
time.sleep(5)
fileops(filename="UNIQUESEC",operation="del")
print("Dosya Silindi")
os.system("ls -la")