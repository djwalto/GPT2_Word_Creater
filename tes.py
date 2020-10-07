import booste
in_string = "There once was a little boy who had a very bad temper. His father decided to hand him a bag of nails and said that every time the boy lost his temper, he had to hammer a nail into the fence.  On the first day, the boy hammered 37 nails into that fence.  The boy gradually began to control his temper over the next few weeks, and the number of nails he was hammering into the fence slowly decreased. He discovered it was easier to control his temper than to hammer those nails into the fence."
out_length = 20
out_list = booste.gpt2(
    'ecfb48aa-7bb2-4a37-92d5-f2fc5ed0deed', in_string, out_length)
print(out_list)

out_string = " ".join(out_list)
print(out_string)

in_string = "When I go to bed at night, I think to myself how amazing it was to spend my days doing the things that I love and enjoy.  Each morning, I wake up and think how lucky I am to be alive.  I work from 7 pm to 9. The color of my house is beautiful. I'm a little out of it but I know that I can persist through."
out_length = 50
out_list = booste.gpt2(
    'ecfb48aa-7bb2-4a37-92d5-f2fc5ed0deed', in_string, out_length)
print(out_list)

out_string = " ".join(out_list)
print(out_string)
