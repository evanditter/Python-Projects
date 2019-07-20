class Random:
    def __init__(self, seed):
        self.__n = seed

    def next(self, range):
        self.__n = ((16807 * (self.__n)) % (2147483648 - 1))
        return self.__n % range

    def choose(self, letters):
        size = len(letters)
        return letters[self.next(size)]


class Mnemonic:
    def __init__(self, seed):
        self.__random = Random(seed)
        self.__follow = {'a': '', 'b': '', 'c': '', 'd': '', 'e': '', 'f': '', 'g': '', 'h': '', 'i': '', 'j': '',
                         'k': '', 'l': '', 'm': '', \
                         'n': '', 'o': '', 'p': '', 'q': '', 'r': '', 's': '', 't': '', 'u': '', 'v': '', 'w': '',
                         'x': '', 'y': '', 'z': ''}
        self.__letters = {'0': 'z', '1': 'q', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'prs',
                          '8': 'tuv', '9': 'wxy'}

    def add(self, word):
        follow = self.__follow
        words = list(word)
        size = len(words) - 1

        for i in range(size):
            if words[i] in follow:
                follow[words[i]] += words[i + 1]
            else:
                follow[words[i]] = [words[i + 1]]
            i += 1
        #print(follow) #used to show add is working
        # displays dictionary follow

    def make(self, number):
        follow = self.__follow
        random = self.__random
        letters = self.__letters
        num = list(number)
        mnemonic = ''  #will be the final output for the word constructed
        f = random.choose(letters[num[0]])
        mnemonic += f

        for i in range(len(num) - 1):
            temp = ''
            last = mnemonic[i]
            str = follow[last]
            # print(last, ":",str) used for testing last and str while debugging
            for e in str:
                if e in letters[num[i + 1]]:
                    temp += e
            # print(temp) used to test temp while debugging
            if len(temp) == 0:
                return ''  # returns empty string if no letters left in temp
            f = random.choose(temp)
            mnemonic += f

        return mnemonic

m = Mnemonic(101)

m.add('about')
m.add('after')
m.add('again')
m.add('always')
m.add('an')
m.add('and')
m.add('any')
m.add('apple')
m.add('around')
m.add('as')
m.add('ask')
m.add('away')
m.add('baby')
m.add('back')
m.add('ball')
m.add('bear')
m.add('because')
m.add('bed')
m.add('been')
m.add('before')
m.add('bell')
m.add('best')
m.add('better')
m.add('big')
m.add('bird')
m.add('birthday')
m.add('blue')
m.add('boat')
m.add('both')
m.add('box')
m.add('boy')
m.add('bread')
m.add('bring')
m.add('brother')
m.add('buy')
m.add('by')
m.add('cake')
m.add('call')
m.add('can')
m.add('car')
m.add('carry')
m.add('cat')
m.add('chair')
m.add('chicken')
m.add('children')
m.add('christmas')
m.add('claus')
m.add('clean')
m.add('coat')
m.add('cold')
m.add('come')
m.add('corn')
m.add('could')
m.add('cow')
m.add('cut')
m.add('day')
m.add('does')
m.add('dog')
m.add('doll')
m.add('done')
m.add('dont')
m.add('door')
m.add('down')
m.add('draw')
m.add('drink')
m.add('duck')
m.add('egg')
m.add('eight')
m.add('every')
m.add('eye')
m.add('fall')
m.add('far')
m.add('farm')
m.add('farmer')
m.add('fast')
m.add('father')
m.add('feet')
m.add('find')
m.add('fire')
m.add('first')
m.add('fish')
m.add('five')
m.add('floor')
m.add('flower')
m.add('fly')
m.add('for')
m.add('found')
m.add('from')
m.add('full')
m.add('funny')
m.add('game')
m.add('garden')
m.add('gave')
m.add('girl')
m.add('give')
m.add('giving')
m.add('go')
m.add('goes')
m.add('goodbye')
m.add('got')
m.add('grass')
m.add('green')
m.add('ground')
m.add('grow')
m.add('had')
m.add('hand')
m.add('has')
m.add('head')
m.add('help')
m.add('her')
m.add('here')
m.add('hill')
m.add('him')
m.add('his')
m.add('hold')
m.add('home')
m.add('horse')
m.add('hot')
m.add('house')
m.add('how')
m.add('hurt')
m.add('if')
m.add('in')
m.add('is')
m.add('it')
m.add('its')
m.add('jump')
m.add('just')
m.add('keep')
m.add('kind')
m.add('kitty')
m.add('know')
m.add('laugh')
m.add('leg')
m.add('let')
m.add('letter')
m.add('light')
m.add('little')
m.add('live')
m.add('long')
m.add('look')
m.add('made')
m.add('make')
m.add('man')
m.add('many')
m.add('may')
m.add('me')
m.add('men')
m.add('milk')
m.add('money')
m.add('morning')
m.add('mother')
m.add('much')
m.add('my')
m.add('myself')
m.add('name')
m.add('nest')
m.add('never')
m.add('night')
m.add('not')
m.add('of')
m.add('off')
m.add('old')
m.add('once')
m.add('one')
m.add('only')
m.add('open')
m.add('or')
m.add('over')
m.add('own')
m.add('paper')
m.add('party')
m.add('pick')
m.add('picture')
m.add('pig')
m.add('play')
m.add('pull')
m.add('put')
m.add('rabbit')
m.add('rain')
m.add('read')
m.add('red')
m.add('right')
m.add('ring')
m.add('robin')
m.add('round')
m.add('run')
m.add('said')
m.add('santa')
m.add('school')
m.add('see')
m.add('seed')
m.add('seven')
m.add('shall')
m.add('sheep')
m.add('shoe')
m.add('show')
m.add('sing')
m.add('sister')
m.add('sit')
m.add('six')
m.add('sleep')
m.add('small')
m.add('snow')
m.add('some')
m.add('song')
m.add('squirrel')
m.add('start')
m.add('stick')
m.add('stop')
m.add('street')
m.add('sun')
m.add('table')
m.add('take')
m.add('tell')
m.add('ten')
m.add('thank')
m.add('the')
m.add('their')
m.add('them')
m.add('then')
m.add('these')
m.add('thing')
m.add('think')
m.add('those')
m.add('three')
m.add('time')
m.add('to')
m.add('today')
m.add('together')
m.add('top')
m.add('toy')
m.add('tree')
m.add('try')
m.add('two')
m.add('up')
m.add('upon')
m.add('us')
m.add('use')
m.add('very')
m.add('walk')
m.add('warm')
m.add('wash')
m.add('watch')
m.add('water')
m.add('way')
m.add('we')
m.add('were')
m.add('when')
m.add('where')
m.add('which')
m.add('why')
m.add('wind')
m.add('window')
m.add('wish')
m.add('wood')
m.add('work')
m.add('would')
m.add('write')
m.add('yellow')
m.add('you')
m.add('your')

# Given Outputs
print('"' + m.make('6862377') + '"')  # "ounadrr"
print('"' + m.make('6862377') + '"')  # "ounadrs"
print('"' + m.make('6862377') + '"')  # "ntobers"
print('"' + m.make('6862377') + '"')  # "ouncerr"
print('"' + m.make('6862377') + '"')  # "ntoadrr"
print('"' + m.make('6862377') + '"')  # "muncess"
print('"' + m.make('6862377') + '"')  # "ounadrs"
print('"' + m.make('6862377') + '"')  # "munadrs"
print('"' + m.make('6862377') + '"')  # "ouncers"
print('"' + m.make('6862377') + '"')  # "otoadrr"

print('--------')  # to differentiate the tests

#tests not given in project assignment

print('"' + m.make('2222227') + '"')  # ""
print('"' + m.make('2222227') + '"')  # "cababas"
print('"' + m.make('2222227') + '"')  # "cabbabr"
print('"' + m.make('2222227') + '"')  # "bababbr"

print('--------')

print('"' + m.make('2322223') + '"')  # "adababe"
print('"' + m.make('2222223') + '"')  # "bbabbad"
print('"' + m.make('2222223') + '"')  # "bacabad"
print('"' + m.make('2222223') + '"')  # "bacabad"
print('"' + m.make('2222223') + '"')  # "bbababe"

print('--------')

print('"' + m.make('2862377') + '"')  # "cunadrs"
print('"' + m.make('2862377') + '"')  # "aunadrr"
print('"' + m.make('2862377') + '"')  # "cumafrr"
print('"' + m.make('2862377') + '"')  # "buncerr"

print('--------')

print('"' + m.make('9999999') + '"')  # ""
print('"' + m.make('9999999') + '"')  # ""
print('"' + m.make('9999999') + '"')  # ""
# These three results make since because no word would have letters with only w x and y

print('--------')

#Works with different amount of digits as well, was trying to get cell
print('"' + m.make('2355') + '"')  # "cell"
print('"' + m.make('2355') + '"')  # "cell"
print('"' + m.make('2355') + '"')  # "bell"
print('"' + m.make('2355') + '"')  # "cell"
print('"' + m.make('2355') + '"')  # "afll"
print('"' + m.make('2355') + '"')  # "cell"
