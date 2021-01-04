import os
import re


def Punctuation(data_txt):
    # punctuation marks
    punctuations = '''!()[]{};:'"\,<>./?@#$%^&*_~'''

    # check for any punctuation and replace it with ' '
    for x in data_txt:
        if x in punctuations:
            data_txt = data_txt.replace(x, " ")
    data_txt = re.sub("\s\s+", " ", data_txt)
    return data_txt


def main():

    input_file = input("Please enter your input file full-path:\n")

    if (not os.path.isfile(input_file)) or (not os.path.splitext(input_file)[1]==".txt") or (not os.access(input_file, os.R_OK)):
        print("ERROR: Program stopped due to one of the below reasons:\n 1. The file doesn't exist, or\n 2. Mandatory file path parameter is not specified, or\n 3. Incorrect file path, or\n 4. Incorrect file format (should be .txt)., or\n 5. Insuffient file read authorization.")
    else:
        output_file = input("Please enter desired output file name (example: wc_report.txt, my_report.txt..) :\n")

        # check for file name, and correct file extension (should be .txt) - create default output file
        if (not output_file) or (not output_file.endswith(".txt")):
            output_file='wc_report.txt'
            print("Default output file name 'wc_report.txt'")

        data = ''
        with open(input_file, 'r') as f:
            data = f.read()

        if not data:
            print("ERROR: input file '{0}' is empty".format(input_file))
            return None
        else:
            # Remove punctuations, except Hyphenated (-) and make the data case insensitive by changing it to lower
            data =  Punctuation(data.lower())

            # Get word count
            words=[]
            words = data.split(' ')

            word_count_dict={}
            # Preserve word count in a dictionary
            for item in words:
                if item in word_count_dict.keys():
                    word_count_dict[item]=word_count_dict[item]+1
                else:
                    word_count_dict[item]=1

            #Sort in decending order
            sorted_word_count_dict={k: v for k,v in sorted(word_count_dict.items(), key=lambda item: item[1], reverse=True)}

            f = open(output_file,'w+')
            f.write("# The total word count : "+ str(len(words))+"\n"+"# Total of unique words : "+str(len(list(set(words))))+"\n\n"+"# The top 10 words based on their word count, showing the word and how many times it appeared : \n")
            f.write("Word - Count" + "\n")

            # fetch only top 10 words
            for item in list(sorted_word_count_dict.items())[:10]:
                f.write(str(item[0]) + " : "+str(item[1])+"\n")

            f.close()
            print("Output stored to '{0}'".format(output_file))


if __name__ == '__main__':
    main()