#Homework Lesson 12 - Files and CLI

import argparse

def modify_song(input_file, output_file, additional_lyrics=None, flag=False):
  with open(input_file, 'r') as input_file:                                         #opens exisitng file (song) in reader mode
    lyrics = input_file.read()

  #Replace "five hundred" with "500" everywhere in the song
  lyrics = lyrics.replace("five hundred", "500")

  #Changes song's text to capital letters
  lyrics = lyrics.upper()

  # Optional argument operation
  if additional_lyrics:
    lyrics += "\n" + additional_lyrics                                               #add additional lyrics lines to the song (on a new line)

  # Boolean flag operation
  if flag:
    lyrics = lyrics + "\n" + lyrics                                                 #Repeat the songs lyrics twice if Flag is raised (on a new line)

  with open(output_file, 'w') as output_file:
    output_file.write(lyrics)                                                       #write out the result to new file


def main():
  parser = argparse.ArgumentParser(description='Process song lyrics.')
  parser.add_argument('input_file', type=str, help='Input file name')
  parser.add_argument('output_file', type=str, help='Output file name')
  parser.add_argument('--opt', type=str, help='Add more lines of lyrics if you wish')
  parser.add_argument('--flag', action='store_true', help='Repeat twice if your favourite song')

  args = parser.parse_args()

  modify_song(args.input_file, args.output_file, args.opt, args.flag)

if __name__ == "__main__":
    main()


##########################
#run on command line using the optional args: python lesson12_homework.py song.txt modified_song.txt --opt "Da-da da da (Da-da da da) Da-da da da (Da-da da da) Da-da dum diddy dum diddy dum diddy da da da" --flag
#or without optional arguments: python lesson12_homework.py song.txt modified_song.txt