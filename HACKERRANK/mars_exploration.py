# A space explorer's ship crashed on Mars! They send a series of SOS messages to Earth for help.

# Letters in some SOS messages are altered by cosmic radiation during transmission. Given the signal
# received by Earth as a string, determine how many letters of the SOS message have been changed by radiation.

# Example
# s = SOTTOS
# The original message was SOSSOS. Two of the message's characters were changed in transit.
#
# Function Description
#
# mars_exploration  has the following parameter(s):
#
# string s: the string as received on Earth
# Returns
#
# int: the number of letters changed during transmission
# Input Format
#
# There is one line of input: a single string.
#
# Constraints
#
#  s will contain only uppercase English letters, ascii[A-Z].


def mars_exploration(s: str) -> int:
    let = 0
    while len(s):
        pal = s[:3]
        s = s[3:]
        if pal[0] != 'S':
            let = let + 1
        if pal[1] != 'O':
            let = let + 1
        if pal[2] != 'S':
            let = let + 1
    return let


print(mars_exploration("SOSSIO"))
