import booste
in_string = "I never knew I could live like this.  My whole life feels like a dream.  When I go to bed at night, I think to myself how amazing it was to spend my days doing the things that I love and enjoy.  Each morning, I wake up and think how lucky I am to be alive."
out_length = 20
out_list = booste.gpt2(
    'ecfb48aa-7bb2-4a37-92d5-f2fc5ed0deed', in_string, out_length)

print(out_list)

out_string = " ".join(out_list)
print(out_string)

in_string = "I never knew I could live like this.  My whole life feels like a dream.  When I go to bed at night, I think to myself how amazing it was to spend my days doing the things that I love and enjoy.  Each morning, I wake up and think how lucky I am to be alive.  I work from 7 pm to 9. The color of my house is beautiful. I'm a little out of it but I know that I can persist through."
out_length = 20
out_list = booste.gpt2(
    'ecfb48aa-7bb2-4a37-92d5-f2fc5ed0deed', in_string, out_length)

print(out_list)

out_string = " ".join(out_list)
print(out_string)
