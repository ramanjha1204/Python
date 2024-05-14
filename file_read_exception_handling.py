try:
    file = open('file.txt', 'r')
    content = file.read()
    print("File content:")
    print(content)
    file.close()

except FileNotFoundError:
    print("File not found.")

except Exception as e:
    print("An error occurred:", e)

finally:
    if 'file' in locals():
        # Check if the file is open before trying to close it
        if not file.closed:
            file.close()
        print("File closed in finally block.")
