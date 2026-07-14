from pypdf import PdfWriter
import os

def main():
    print("Welcome to the PDF Merger!!")
    
    file_track = []
    
    while(True):
        
        user_input = input("Enter the pdf file path: ")
        
        if user_input == "done":
            if len(file_track) < 2:
                print("Incorrect number of files inserted. Try Again.")
            else:
                print("Files successfully loaded")
                break
        else:
             path_exists = os.path.exists(user_input)
             is_pdf = user_input.endswith('.pdf')
             if path_exists and is_pdf == True:
                  file_track.append(user_input)
                  print(f"Files currently being tracked:  {file_track}")
             else:
                  if not os.path.exists(user_input):
                       print("The file path does not exist. Please try again.")
                  else:
                       print("The file is not a PDF file. Please try again.")
    while True:
        output_filename = input("Name your file (must end with .pdf): ")
        
        has_pdf_extension = output_filename.endswith('.pdf')
    
        if not has_pdf_extension:
            filename_with_ext = output_filename + ".pdf"
        else:
            filename_with_ext = output_filename
        if os.path.exists(filename_with_ext):
             confirm = input(f"{filename_with_ext} already exists. Overwrite? (y/n): ")
             if confirm.lower() == "y":
                  break
        else:
             break
    try:
         
        writer = PdfWriter()
    
        for x in file_track:
             writer.append(x)
         
        writer.write(filename_with_ext)
        writer.close()
        print(f"Success! Files merged into {filename_with_ext}")
        
    except Exception as e:
         print(f"An error occured: {e}")
         
         
if __name__ == "__main__":
     while True:
          main()
          
          again = input("Merge another batch? (y/n): ")
          if again.lower() != "y":
               break