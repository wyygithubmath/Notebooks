1.Question 1

E: Could not get lock /var/lib/apt/lists/lock - open (11: Resource temporarily unavailable)
E: Unable to lock directory /var/lib/apt/lists/

Answer
```
ps -aux | grep apt-get
sudo kill PID

```

3. delete softs
```
sudo apt remove --purge
```

