# Command

## 0. `help`

## 1. SystemInfo

|        cmd        |  note  |
| :----------------: | :-----: |
|    `uname -a`    | kernel |
| `lsb_release -a` | version |
|     `df -h`     |  disk  |
|    `free -h`    | memory |

## 2. Software

|               cmd               |    note    |
| :------------------------------: | :---------: |
|       `sudo apt update`       |  app list  |
|       `sudo apt upgrade`       | upgrade app |
| `sudo apt install [pack name]` |   install   |
| `sudo apt remove [pack name]` |  uninstall  |
|    `apt search [key word]`    |            |

## 3. Document Operation

|             cmd             |                            note                            |
| :-------------------------: | :--------------------------------------------------------: |
|           `ls`           |                     list `-a` `-l`                     |
|        `cd [path]`        | change directory -  . (cur)  .. (back)  / (root)  ~ (home) |
|    `mkdir [dir name]`    |                            make                            |
|    `rmdir [dir name]`    |                           remove                           |
|    `touch [doc name]`    |                            make                            |
|      `rm [doc name]`      |                           delete                           |
|     `cat [doc name]`     |                            read                            |
|     `less [doc name]`     |        `[cmd 2>&1]\|less`scroll output  `q` quit        |
|  `vim [doc name]` `vi`  |                            edit                            |
| `cp [src doc] [dist doc]` |                            copy                            |
| `mv [src doc] [dist doc]` |                       move / rename                       |
|           `pwd`           |                            path                            |
|          `code`          |                           vscode                           |
|          `open`          |                            html                            |
|          `clear`          |                                                            |
|          `chmod`          |                                                            |

## 4. Compile & Run C

|                                                                                              cmd                                                                                              |                                                               note                                                               |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------: |
|                                                                                        **Stage**                                                                                        |                                                                                                                                  |
| `gcc -E hello.c -o hello.i` (`-E` Preprocessing)  `gcc -S hello.c -o hello.s` (`-S` Compilation)  `gcc -c hello.c -o hello.o` (`-c` Assembly)  `gcc hello.c -o hello` (Linking) | `gcc [src1] [src2] ... -o [out]` (`-c .c``.o -o`in a way)  `-E/-S/-c [src]` (out file stage)  `-o [out]` (out file name) |
|                                                                                          `./[out]`                                                                                          |                                                               run                                                               |
|                                                                                       **Insert**                                                                                       |                                                   `gcc -Wall -g -c hello.c`                                                   |
|                                                                                            `-g`                                                                                            |                                                            debug info                                                            |
|                                                                                           `-Wall`                                                                                           |                                                             warning                                                             |

## 5. Process Management

|               cmd               |     note     |
| :------------------------------: | :-----------: |
|            `ps anx`            |   read all   |
| `ps -ef \| grep [process name]` | read specific |
|           `kill PID`           |   terminate   |
|             `top`             | realtime read |
|             `jobs`             |   read back   |
|             Ctrl + Z             |  stop front  |
|              `bg`              |    to back    |
|              `fg`              |   to front   |

# Virtual Machine

#### Configure

VitualBox - Ubuntu ISO (CD drive) - Install

#### Test

|        content        |                                                                  cmd                                                                  |
| :--------------------: | :-----------------------------------------------------------------------------------------------------------------------------------: |
|   **Network**   |                                                        `ping -c 4 baidu.com`                                                        |
| **SystemUpdate** |                                             `sudo apt update`  `sudo apt upgrade -y`                                             |
| **InstallTool** | `sudo apt install [tool name] -y`  `build-esstential` (compile)  `gdb valgrind` (debug)  `vim ` (edit)  `make` (auto build) |
|    **Verify**    |                                       `gcc --version`  `g++ --version`  `make --version`                                       |

# Vim

|     op     |      shell      |
| :--------: | :-------------: |
|  EditMode  |      `i`      |
| SearchMode |      `/`      |
| NormalMode |     `esc`     |
|  CtrlMode  |      `:`      |
|    Save    |     `:w`     |
|    Exit    | `:q` /`:q!` |
|    S&E    | `:wq` /`:x` |

# Nginx

#### Web Listen

|                                cmd                                |     note     |
| :---------------------------------------------------------------: | :----------: |
|                        `ssh [NAME]@[IP]`                        | cloud server |
|                        `sudo apt update`                        |              |
|                   `sudo apt install nginx -y`                   |   port 80   |
|                  `sudo systemctl start nginx`                  |     run     |
|                  `sudo systemctl status nginx`                  |              |
| `sudo systemctl enable nginx`, `sudo systemctl disable nginx` |  auto start  |

#### Page Configure

**1. default** `etc/nginx/sites-available/default` -- `var/www/html/index.nginx-debian.html`
**2. web address (IP + port + doc)**: http://127.0.0.1:8080
**3. personal configuration**: `sudo vim /etc/nginx/sites-enabled/default`: `root /var/www/html` -- `root /home/[user dir]/[new dir]`
**4. reload status**: `sudo nginx -t`, `sudo systemctl reload nginx`
**5. permission**: `sudo chmod o+x /home/[name]`

# Git

|                                               cmd                                               |                                   note                                   |
| :---------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------: |
|                                         **local**                                         |                                                                          |
|                                   `sudo apt install git -y`                                   |                                                                          |
|         `git config --global user.name [name]git config --global user.email [email]`         |                                                                          |
|                                          `git init`                                          |                        `cd [content]`, `.git`                        |
|                                         `git status`                                         |                                                                          |
|                                     `git add [doc name]`                                     |                       track, `git add .` for all                       |
|                                 `git commit -m "description"`                                 |                                                                          |
|                                           `git log`                                           |                                                                          |
|                                        **remote**                                        |      **SSH:** `git@github.com:[name]/[repository name].git`      |
| `ssh-keygen -t ed25519 -C [email]` (generate key)  `cat ~/.ssh/id_ed25519.pub` (public key) | **add ssh key**: GitHub - Settings - SSH and GPG keys - New SSH key |
|                                    `ssh -T git@github.com`                                    |                      **verify ssh** available                      |
|        `git remote add origin git@github.com:[name]/[dir name].git`  `git remote -v`        |                        **link** remote repo                        |
|                                         `git branch`                                         |                      branch name `main`/`master`                      |
|                              `git push -u origin [branch name]`                              |             `-u` first time  **add - commit - push**             |
|                       `git clone git@github.com:[name]/[repo name].git`                       |                         **clone** to server                         |
|                                          `git pull`                                          |                                                                          |
|                                        `git checkout`                                        |                           discard not committed                           |

# Make

#### Rule Edit

* **base**

```
# Makefile
exe:src1.c src2.c header.h
    gcc src1.c src2.c -o exe
```

* **template**

```
# Makefile
# Configure Field (Modify)
CC = gcc                # compiler
CFLAGS = -Wall -g       # warning + debug
TARGETS = main child     # out files name
HEADERS = common.h      # pulic header file
MAIN_EXE = main         # run file

# Rule Field (Tab)
.PHONY: all clean run

all: $(TARGETS)         #default dest

%: %.c $(HEADERS)		# `make (xxxx)`
    $(CC) $(CFLAGS) $< -o $@

clean:
    rm -f $(TARGETS)

run: all
    ./$(MAIN_EXE)
```

#### Pack Build

| cmd (defined) |     op     |
| :------------: | :---------: |
|    `make`    | compile all |
| `make clean` |  clean all  |
|  `make run`  |   run all   |
| `make [out]` |   run one   |

# Tmux

* **Enter** `Ctrl + B`

|      op      |       cmd       |
| :-----------: | :-------------: |
|  horizontal  |      `%`      |
|   vertical   |      `"`      |
| switch window | `[arrow key]` |
|     close     |    `exit`    |