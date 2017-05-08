from fabric.operations import local as localrun



def run_go():
    localrun("cd server_go && docker build -t workshop_go ." )
    localrun("docker run -it --rm -p 9090:9090 workshop_go")


def convey():
    localrun("docker-compose up -d" )

def app_docker(project="server_beego"):
	#localrun("cd src/%s && docker run --rm -v `pwd`:/src -v /var/run/docker.sock:/var/run/docker.sock centurylink/golang-builder" % project)
	localrun("docker run --rm -v `pwd`:/go/src/workshop -w /go/src/workshop/%(project)s -e CGO_ENABLED=0  workshop_test go build --ldflags '-extldflags \"-static\"' -a --installsuffix cgo -o %(project)s" % ( { 'project' : project } ))  
	build_docker("%s" % project , project , " --no-cache ")

# Generic builder
def build_docker(path="dockers/nginx" , name="nginx-siteboost" , args=''):
	#localrun("cd %s cp -Rf keys %s " % ( env.wd , docker_path  ) )
	localrun("cd %s && docker build %s -t %s ." % ( path , args , name ) )