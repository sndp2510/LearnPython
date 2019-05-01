'''
Created on Apr 30, 2019

@author: Scorpion
'''
import sys 

def main():
    print 'Hello there', sys.argv[1]
    print repeat ('Yay', False)
    print repeat ('woo hoo', True)
    ##help(sys) 
    #stringDemo()
    print " >> 95,'bad'"
    conditionalDemo(95,'bad')
    print " >> 130,'terrible'"
    conditionalDemo(130,'terrible')
    print " >> 85,'confused'"
    conditionalDemo(85,'confused')

def conditionalDemo (speed, moody):
    if speed >=80:
        print 'License and registration please.'
        if speed >= 100  or moody == 'terrible' :
            print 'you have the right to remain silent'
        elif moody == 'bad' or speed >=90:
            print 'i am going to have write you a ticket.'
        else:
            print 'Lets try to keep it under 80 ok?'
        

def stringDemo():
    s='hi'
    print s[1]
    print len(s)
    print s + ' there'
    pi = 3.14
    text = 'The value of pi is ' + str(pi)
    print text
    raw = r'this\t\n and that'
    print raw
    
    multi = """It was the best of times.
    It was the worst of times."""
    print multi
    
    print multi.lower()
    print multi.find('times')
    splitArr = multi.split()
    print len(splitArr)
    print '---'.join(splitArr)
    s = r'He\lo'
    print s[1:4]
    print s[:4]
    print s[4:]
    print s[:-5]
    print s[-5:]
    
    text= ('%d little pigs come out,'
           ' or I will %s, I will %s, '
           'and I will blow your %s down.'
           % (3, 'huff', 'puff','house'))
    print text




def repeat (s,exclaim):
    """
    this a documentation string
    """
    result = s*3
    if exclaim:
        result = result + '!!!'
    return result


if __name__ == '__main__':
    main()