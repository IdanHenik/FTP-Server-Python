
# FTP-Server in Python


![App Screenshot](https://i.postimg.cc/bY3436Fm/what-is-file-transfer-protocol.png)



FTP Server (which stands for File Transfer Protocol Server) is a software application which enables the transfer of files from one computer to another.

([If you want to know more about FTP Protocol](https://www.techtarget.com/searchnetworking/definition/File-Transfer-Protocol-FTP)
)

## Requirements

1. port 20 & port 21 in the machine MUST be open.

2. make sure you got pyftpdlib installed,
if not just insert the CLI the next line

```bash
  pip install pyftpdlib
```


## Step 1

make a source directory and make sure 

`PATH=<path to directory>` after that add a file for testing.

![step 1](https://i.postimg.cc/BQd3BYXd/image.png)



## Step 2
let's run the program by :


```bash
  Python FTP_Server.py
```
if your CLI get this output it mean its working !
![step 2](https://i.postimg.cc/cL2cH3k7/image.png)
## Step 3
Now we need to access the server by typing the ip of the machine
in the website url, `ftp://<ip>`

then enter username and password for the FTP server wich defined defaulty as `username=admin` `pass=adminpass`.

![Step 3](https://i.postimg.cc/gcK7SMrx/image.png)

then if you see the next stage like in the following picture:

![Step 3.1](https://i.postimg.cc/8k3vSG79/image.png)

## Congratulations You have a FTP Server on your machine !