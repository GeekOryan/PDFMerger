'''
1. Display welcome message
2. Loop: ask user for a PDF file path (or type "done" to finish)
3. If input is "done":
     - If fewer than 2 files added, show error, keep looping
     - If 2+ files added, show "Files loaded" + exit the collection loop
4. If input is a file path:
     - Check path exists AND ends in .pdf
     - If invalid, show specific error, loop again
     - If valid, add to list, display running list of files added so far
5. Ask for output filename
     - Auto-append .pdf if user didn't type it
6. Check if that filename already exists
     - If yes, ask for confirmation to overwrite (y/n)
     - If "n", ask for a new filename
7. Attempt the merge
     - If it fails, show exact error + suggested fix
     - If it succeeds, show success message with output filename
8. Ask: merge another batch, or exit
     - If another batch, loop back to Step 2
     - If exit, close program

'''

from pypdf import PdfMerger
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
                       
    output_filename = input("Name your file (must end with .pdf): ")
        
    has_pdf_extension = output_filename.endswith('.pdf')
    
    if not has_pdf_extension:
         filename_with_ext = output_filename + ".pdf"
    else:
         filename_with_ext = output_filename