import subprocess

text = b'''
hello world to joshua alana the best software engineer in the world
this is the test file for the python scripting
thank you
'''

p = subprocess.Popen(['wc'],
                     stdout = subprocess.PIPE,
                     stdin = subprocess.PIPE)

stdout, stderr = p.communicate(text)

out = stdout.decode('utf-8')
err = stderr.decode('utf-8')
