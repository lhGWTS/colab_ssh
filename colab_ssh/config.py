"""Install and config many of the tool that I use for my day to day work"""

import secrets
import subprocess

from colab_ssh.utils import AptManager, run_command


def config_root_password(msg):
    """
    Create a random password, set it for the root user and attach it to the final log
    """
    root_password = secrets.token_urlsafe()
    subprocess.run(
        ["chpasswd"], input=f"root:{root_password}", universal_newlines=True, check=False)
    msg += "✂️"*24 + "\n"
    msg += f"Root password: {root_password}\n"
    msg += "✂️"*24 + "\n"
    return msg


def install_apt_pkg():
    """
    Install my own usefull package, won't explain more about why :P
    """
    apt_manager = AptManager()
    apt_manager.update()
    apt_manager.commit()
    #all_pkg = ['nano', 'htop', 'tmux', 'vim', 'cmake','fish','aria2',
    #           'libncurses5-dev', 'libncursesw5-dev', 'git',
    #           'tree', 'zip', 'expect', 'pigz', 'pv']
    all_pkg = ['vim', 'cmake','fish','aria2','build-essential','htop',
               'libncurses5-dev', 'libncursesw5-dev', 'git','file',
               'tree', 'zip', 'expect', 'pigz', 'pv','zstd','powershell']
    apt_manager.install_pkg(*all_pkg)
    apt_manager.commit()


def install_nvtop():
    """
    Install nvtop which is an amazing tool for monitoring NVIDIA GPU
    """
    print("Installing nvtop")
    command = """git clone https://github.com/Syllo/nvtop.git
                 mkdir -p nvtop/build && cd nvtop/build && cmake .. && make && make install && cd
                 rm -rf nvtop"""
    run_command(command)


def install_pip_dependencies():
    """
    Install pip dependencies that I use everyday
    """
    print("Installing pip dependencies")
    command = "pip3 install imgaug clearml ipdb"
    run_command(command)


def config_bashrc():
    """
    Add usefull bash configuration that I use everyday
    """
    print("Configuring .bashrc")
    command = """echo "export LD_LIBRARY_PATH=/usr/lib64-nvidia" >> /root/.bashrc
                 echo "alias ls='ls --color'" >> ~/.bashrc
                 echo "alias ll='ls --color -l'" >> ~/.bashrc
                 echo "alias l='ls --color -lA'" >> ~/.bashrc
                 echo "alias cpwd='pwd|pbcopy'" >> ~/.bashrc"""
    run_command(command)


def install_gdrive_rclone():
    """
    Install gdrive and rclone, which are the CLI that I use to interact with
    various clould storage services.
    """
    print("Installing gdrive and rclone")
    command = """wget -q https://github.com/lamhoangtung/gdrive/releases/download/linux-x64/gdrive-linux-x64
                 mv gdrive-linux-x64 gdrive
                 chmod +x gdrive
                 install gdrive /usr/local/bin/gdrive
                 rm -rf gdrive
                 curl https://rclone.org/install.sh | bash"""
    run_command(command)


def install_fzf():
    """
    Install fzf
    """
    print("Installing fzf")
    command = """git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
                 yes | ~/.fzf/install"""
    run_command(command)


def install_packages_microsoft_prod():
    """
    Install packages-microsoft-prod
    """
    print("Installing packages-microsoft-prod")
    command = """wget -q https://packages.microsoft.com/config/ubuntu/18.04/packages-microsoft-prod.deb
                 sudo dpkg -i packages-microsoft-prod.deb
                 """
    run_command(command)


def install_vim_tmux():
    """
    Install my custom vim and tmux configuration
    """
    print("Installing custom vim and tmux")
    command = """curl -L https://github.com/lamhoangtung/dotfile/raw/linux/install_vim.sh | bash
                 wget https://github.com/lamhoangtung/dotfile/raw/linux/.tmux.conf -P ~"""
    run_command(command)


def install_common_tool():
    """
    Install many of the tool that I use for my day to day work. Other might want to
    modify this function.
    """
    config_bashrc()
    install_packages_microsoft_prod()
    install_apt_pkg()
    install_fzf()
    #install_nvtop()
    #install_pip_dependencies()
    #install_gdrive_rclone()
    #install_vim_tmux()
