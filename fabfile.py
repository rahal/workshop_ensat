from fabric.operations import local as localrun



def run_go():
    localrun("cd server_go && docker build -t workshop_go ." )
    localrun("docker run -it --rm -p 9090:9090 workshop_go")

def run_go_compose():
    localrun("cd server_go && docker build -t workshop_go ." )
    localrun("docker run -it --rm -p 9090:9090 workshop_go")

def convey():
    localrun("docker-compose up -d" )