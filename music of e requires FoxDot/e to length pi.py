import time
e='2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274'
pi='3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
pitch=list(str(e))
pitch.remove('.')
for i in range(len(pitch)):
    pitch[i]=int(pitch[i])
length=list(str(pi))
length.remove('.')
for i in range(len(length)):
    length[i]=3/(int(length[i])+1)
if len(e)==len(pi):
    p1 >> pluck(pitch, dur=length)
    time.sleep(sum(length))
    quit()
