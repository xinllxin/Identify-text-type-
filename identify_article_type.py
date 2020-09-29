#final project



#functions 
def clean_text(txt): 
    ''' takes a string of text txt as a parameter and returns a list containing
        the words in txt after it has been “cleaned”. This function will be used
        when you need to process each word in a text individually, without
        having to worry about punctuation or special characters.
    '''

    txt = txt.replace(',','')
    txt = txt.replace('(','')
    txt = txt.replace(')','')
    txt = txt.replace('.','')
    txt = txt.replace('?','')
    txt = txt.replace("'",'')
    txt = txt.replace('''"''','')
    txt = txt.lower()
    txt = txt.split()

    return txt


def stem(s):
    ''' accepts a string as a parameter. The function should then return the stem of s.'''

    words = clean_text(s)
    stems = []
    
    if len (words) > 1:
        
        for word in words:
            if len(word) > 4:
                if word[-3:] == 'ing':
                    if word[-4] == word[-5]:
                        word = word[:-4]
                    else:
                        word = word[:-3]
                    stems += [word]
                elif word[-1:] == 's':
                    word = word[:-1]
                    stems += [word] 
                elif word[-2:] == 'er':
                    if word[-3] == word[-4]:
                        word = word[:-3]
                    else:
                        word = word[:-2]
                    stems += [word] 
                elif word[-4:] == 'tive':
                    word = word [:-3]
                    stems += [word] 
                elif word[-4:] == 'sive':
                    word = word[:-3]
                    stems += [word] 
                elif word[-2:] == 'ed':
                    if word [-2] == word[-3]:
                        word = word[:-3]
                    else:
                        word = word[:-2]
                    stems += [word] 
                elif word[-3:] == 'ble':
                    word = word[:-3]
                    stems += [word] 
                elif word[-3:] == 'lly':
                    word = word[:-3]
                    stems += [word] 
                elif word[-4:] == 'ment':
                    word = word[:-4]
                    stems += [word] 
                elif word[-4:] == 'tion':
                    word = word[:-4]
                    stems += [word] 
                elif word[-4:] == 'ches':
                    word = word[:-2]
                    stems += [word] 
                elif word[-3:] == 'ful':
                    word = word[:-3]
                    stems += [word]
            else:
                stems += [word]


    elif len(words) == 1: 
        if len(words[0]) > 4:
            if words[0][-3:] == 'ing':
                if words[0][-4] == words[0][-5]:
                    words[0] = words[0][:-4]
                else:
                    words[0] = words[0][:-3]
                stems += [words[0]] 
            elif words[0][-1:] == 's':
                words[0] = words[0][:-1]
                stems += [words[0]] 
            elif words[0][-2:] == 'er':
                if words[0][-3] == words[0][-4]:
                    words[0] = words[0][:-3]
                else:
                    words[0] = words[0][:-2]
                stems += [words[0]] 
            elif words[0][-4:] == 'tive':
                words[0] = words[0] [:-4]
                stems += [words[0]] 
            elif words[0][-4:] == 'sive':
                words[0] = words[0][:-4]
                stems += [words[0]] 
            elif words[0][-2:] == 'ed':
                if words[0] [-2] == words[0][-3]:
                    words[0] = words[0][:-3]
                else:
                    words[0] = words[0][:-2]
                stems += [words[0]] 
            elif words[0][-3:] == 'ble':
                words[0] = words[0][:-3]
                stems += [words[0]] 
            elif words[0][-3:] == 'lly':
                words[0] = words[0][:-3]
                stems += [words[0]] 
            elif words[0][-4:] == 'ment':
                words[0] = words[0][:-4]
                stems += [words[0]] 
            elif words[0][-4:] == 'tion':
                words[0] = words[0][:-4]
                stems += [words[0]] 
            elif words[0][-4:] == 'ches':
                words[0] = words[0][:-2]
                stems += [words[0]] 
            elif words[0][-3:] == 'ful':
                words[0] = words[0][:-3]
                stems += [words[0]]

        else:
            stems += [word[0]]
            
    return stems


def compare_dictionaries(d1,d2):
    ''' take two feature dictionaries d1 and d2 as inputs, and it should
        compute and return their log similarity score.
    '''
    import math

    score = 0
    total = 0
    for key in d1:
        total += d1[key]
    for key in d2:
        if key in d1:
            score += math.log(d1[key]/total) * d2[key]  
        else:
            score += math.log(0.5/total) * d2[key]
    return score




#in the class

class TextModel:

    def __init__(self,model_name):
        '''constructs a new TextModel object by accepting a string model_name as
           a parameter and initializing the following three attributes:
        '''
        self.model_name = model_name
        self.name = model_name
        self.words = {}             #number of times each word appear
        self.word_lengths = {}      #number of times each word length appears
        self.stems = {}             #number of times each word stem appears in the texr
        self.sentence_lengths = {}  #number of times each sentence length appears
        self.paragraph_lengths = {} #number of times each paragraph length appears

    def __repr__(self):
        ''' returns a string that includes the name of the model as well as the
            sizes of the dictionaries for each feature of the text.
        '''
        s = 'text model name: ' + self.model_name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  number of paragraph lengths: ' + str(len(self.paragraph_lengths))
        return s


    def add_string(self,s):
        ''' adds a string of text s to the model by augmenting the feature
            dictionaries defined in the constructor. It should not explicitly
            return a value.
        '''
        word_list = clean_text(s)
        for w in word_list:
            if w in self.words:
                self.words[w] += 1

            else:
                self.words[w] = 1

        for w in word_list:
            if len(w) in self.word_lengths:
                self.word_lengths[len(w)] += 1
            else:
                self.word_lengths[len(w)] = 1

        stem_list = stem(s)

        for stm in stem_list:
            if stm in self.stems:
                self.stems[stm] += 1
            else:
                self.stems[stm] = 1


        sentence_list = s.replace('? ','#').replace('. ','#').replace('! ','#').split('#')
        
      

        for sent in sentence_list:
           
            if len(sent.split()) in self.sentence_lengths:
                self.sentence_lengths[len(sent.split())] += 1
            else:
                self.sentence_lengths[len(sent.split())] = 1

       
        

        paragraph_list = s.split('\n')
        for p in paragraph_list:
            
            if len(p.split())in self.paragraph_lengths:
                self.paragraph_lengths[len(p.split())] += 1
            else:
                self.paragraph_lengths[len(p.split())] = 1
       


    def add_file(self,filename):
        ''' adds all of the text in the file identified by filename to the model.
            It should not explicitly return a value.
        '''
        f = open(filename, 'r', encoding='utf8', errors='ignore')

        entire_file  = f.read()
        self.add_string(entire_file)

    def save_model(self):
        ''' saves the TextModel object self by writing its various feature
            dictionaries to files. There will be one file written for each
            feature dictionary.
        '''
        f_words = open(self.name + '_' + 'self_words', 'w')   
        f_words.write(str(self.words))
        f_words.close()

        f_word_lengths = open(self.name + '_' + 'self_word_lengths', 'w')  
        f_word_lengths.write(str(self.word_lengths))
        f_word_lengths.close()

        f_stems = open(self.name + '_' + 'self_stems','w' )
        f_stems.write(str(self.stems))
        f_stems.close()

        f_sentence_lengths = open(self.name + '_' + 'self_sentence_lengths', 'w')
        f_sentence_lengths.write(str(self.sentence_lengths))
        f_sentence_lengths.close()

        f_paragraph_lengths = open(self.name + '_' + 'self_paragraph_lengths', 'w')
        f_paragraph_lengths.write(str(self.paragraph_lengths))
        f_paragraph_lengths.close()



    def read_model(self):
        ''' reads the stored dictionaries for the called TextModel object
            from their files and assigns them to the attributes of the called
            TextModel.
        '''

        f_words = open(self.name + '_' + 'self_words', 'r')
        d_words_str = f_words.read()
        f_words.close()
        self.words = dict(eval(d_words_str))
       
        
        f_word_lengths = open(self.name + '_' + 'self_word_lengths', 'r')
        d_word_lengths_str = f_word_lengths.read()
        f_word_lengths.close()
        self.word_lengths = dict(eval(d_word_lengths_str))

        f_stems = open(self.name + '_' + 'self_stems', 'r' )
        d_stems_str = f_stems.read()
        f_stems.close()
        self.stems = dict(eval(d_stems_str))

        f_sentence_lengths = open(self.name + '_' + 'self_sentence_lengths','r')
        d_sentence_str = f_sentence_lengths.read()
        f_sentence_lengths.close()
        self.sentence_lengths = dict(eval(d_stems_str))

        f_paragraph_lengths = open(self.name + '_' + 'self_paragraph_lengths', 'r')
        d_paragraph_str = f_paragraph_lengths.read()
        f_paragraph_lengths.close()
        self.paragraph_lengths = dict(eval(d_paragraph_str))


    def similarity_scores(self, other):
        ''' computes and returns a list of log similarity scores measuring the
            similarity of self and other – one score for each type of feature (words,
            word lengths, stems, sentence lengths, and your additional feature). You
            should make repeated calls to compare_dictionaries, and put the resulting
            scores in a list that the method returns.
        '''
        a = compare_dictionaries(other.words,self.words)
        b = compare_dictionaries(other.word_lengths,self.word_lengths)
        c = compare_dictionaries(other.stems,self.stems)
        d = compare_dictionaries(other.sentence_lengths,self.sentence_lengths)
        e = compare_dictionaries(other.paragraph_lengths,self.paragraph_lengths)
        return [a,b,c,d,e]


    def classify(self, source1, source2):
        ''' compares the called TextModel object (self) to two other “source”
            TextModel objects (source1 and source2) and determines which of
            these other TextModels is the more likely source of the called TextModel.
        '''
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        scores1_sum = self.similarity_scores(source1)[0] + self.similarity_scores(source1)[1] + self.similarity_scores(source1)[2] +self.similarity_scores(source1)[3] + self.similarity_scores(source1)[4]
        scores2_sum = self.similarity_scores(source2)[0] + self.similarity_scores(source2)[1] + self.similarity_scores(source2)[2] +self.similarity_scores(source2)[3] + self.similarity_scores(source2)[4]
        print ('scores for', str(source1.model_name)+':', scores1)
        print('scores for', str(source2.model_name)+':', scores2)
        if scores1_sum > scores2_sum:
            print(self.model_name,'more likely to have come from source1')
        elif scores2 > scores1:
            print(self.model_name,'more likely to have come from scores2')
        else:
            print(self.model_name,'is equally likely to have come from scores1and scores2')


#test functions

def test():
    """ your docstring goes here """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')


    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)

      
    
def run_tests():
    """ your docstring goes here """
    source1 = TextModel('new_york_times')
    source1.add_file('new_york_times.txt')

    source2 = TextModel('shakespeare')
    source2.add_file('shakespeare_source_text.txt')

    new1 = TextModel('boston_globe')
    new1.add_file('boston_globe.txt')
    new1.classify(source1, source2)




    
