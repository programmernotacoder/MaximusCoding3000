import webbrowser
import wolframalpha


def HW():

    while True:
        try:
            question = input("question: ")
                # you need the wolframalpha API to get this key
            client = wolframalpha.Client("Input your wolfram alpha api key here")
            # getting results from wolframalpha
            res=client.query(question)
            print("")
            answer = next(res.results).text
            print(answer, "\n")

            #if the answer cannot be found then google might know the answer! :)
        except StopIteration:
            try:
                print(f"sorry can't find {question}, want to search on google?")
                results = input("y or n: ")
                if "y" in results:
                    #if yes then its getting our answer from google
                    #this means a new_line
                    print("\n")
                    webbrowser.open(f"https://www.google.com/search?q={question}")
            except Exception:
                
                return question

HW()