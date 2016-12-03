# sinkit-local-resolver
RPM Build of Sinkit Local resolver

    spectool -g -R knot-sinkit-container.spec

    rpmbuild -ba knot-sinkit-container.spec

# RPM Yum (DNF) repository
One needs ```createrepo``` tool, i.e. ```dnf -y install createrepo```
## Generating metadata
Then, it's a matter of adding your rpm packages into a directory structure, e.g. ```./Server```, and running: ```createrepo --database Server```. Example result comprises manually created directory structure, manually added rpm packages and automatically generated repodata metadata:

    ./Server
    ./Server/Packages
    ./Server/Packages/knot-sinkit-container-0.0.1-2.fc24.x86_64.rpm
    ./Server/Packages/knot-sinkit-container-0.0.1-2.fc24.src.rpm
    ./Server/repodata
    ./Server/repodata/c1f8b216cc5f32a34b8a5fbd5fc44560a71513e0ec016b2677c3e1681039b270-other.sqlite.bz2
    ./Server/repodata/c23722c4229a29d3f0b604fc3502a0de54c262cece470fc7b4c01b18c16f2abf-other.xml.gz
    ./Server/repodata/97da1d46e78e91ecaa8e14f1835d247f7f7d1413b8f770d55390293f6ec1f141-filelists.sqlite.bz2
    ./Server/repodata/3292ef111ee5bd322e4a43ac162afa7d9e697a986415dd04755ffb59bba2f431-filelists.xml.gz
    ./Server/repodata/ec1e64bb8a98cb268140507b2a94444e4b28327d218e27925a904a04c356a069-primary.sqlite.bz2
    ./Server/repodata/bf601068d8db4d404bfc89f5591c8bc5ca14c7d30e9b63c81b9638c514853c6f-primary.xml.gz
    ./Server/repodata/repomd.xml

To ensure authenticity, rpm packages should be GPG signed. The whole structure could be uploaded to an FTP site.
## Client configuration
Once you have it uploaded somewhere, one could create a repo config, e.g. ```/etc/yum.repos.d/sinkit.repo```:


    [Server]
    name=Sinkit
    # Note the username contains URL encoded entity for character `\'
    baseurl=ftp://sinkit%5Csinkit:mypassword@example.org/site/something/repo/yum/Server
    gpgcheck=0
    # As soon as one is done testing, GPG check should be enabled.
    # gpgcheck=1
    # gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-Sinkit

    
Client then successfully loads packages from the metadata sqlite database we generated:


    [root@box ~]# dnf search sinkit
    Sinkit                                                    603  B/s | 1.2 kB     00:02
    ====== N/S Matched: sinkit ==========================================================
    knot-sinkit-container.x86_64 : Knot DNS Resolver with Sinkit module Docker container.
    knot-sinkit-container.src : Knot DNS Resolver with Sinkit module Docker container.
 
