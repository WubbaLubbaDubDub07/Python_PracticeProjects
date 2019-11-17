class ReverseSentence:
  def __init__(self, sentence="Hello World"):
    self.sentence = sentence

  def reverse(self):
    x= "".join([i for i in self.sentence[::-1]]) ## I changed that one because , when I write 'hello' , output is 'hello' but now output return to 'olleh'
    return x


if __name__ == "__main__":
  sentence = input("Please write your sentence: ")
  reverse_sentence = ReverseSentence(sentence)
  print("The reversed sentence is: ", reverse_sentence.reverse())
