# Challenge Logic Operators
work_tuesday = False
work_thursday = False

"""
- 2 works day = TV 50'
- 1 work day = TV 32'
- 0 work day = No TV
"""

tv_50 = work_tuesday and work_thursday
tv_32 = work_tuesday != work_thursday

print("Tv50={} Tv32={}".format(tv_50, tv_32))

print("I'm {} years old and my name's {}".format(22, "Leandro"))
print("I'm {1} years old and my name's {0}".format("Leandro", 22))
