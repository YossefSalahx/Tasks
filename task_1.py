steps=input("enter your steps: ")
yoursteps=steps.split()
steps=list(map(int,yoursteps))

highest=max(steps)
lowest=min(steps)
avrage=(sum(steps)/len(steps))
sort_step=sorted(steps,reverse=True)

print(f"max value = {highest}")
print("min value = ",lowest)
print("avrage = ",avrage)
print("sort value = ",sort_step)