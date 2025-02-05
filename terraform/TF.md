# Terraform

## Terraform best practices

* Separate terraform files by their responsibility: providers, variables, network, outputs, etc.
* Split files by scopes of work (GitHub, Cloud, Docker)
* Preserve one variable naming style (e.g. snake_case)
* Use `terraform fmt` to keep configs consistent
* Use `terraform validate` to keep configs correct

## Docker

### Terraform state list

```shell
terraform state list

docker_container.nginx
docker_image.nginx
```

### Terraform state show

```shell
terraform state show docker_container.nginx

# docker_container.nginx:
resource "docker_container" "nginx" {
    attach                                      = false
    bridge                                      = [90mnull[0m[0m
    command                                     = [
        "nginx",
        "-g",
        "daemon off;",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = [90mnull[0m[0m
    cpu_shares                                  = 0
    domainname                                  = [90mnull[0m[0m
    entrypoint                                  = [
        "/docker-entrypoint.sh",
    ]
    env                                         = []
    hostname                                    = "5a783323a624"
    id                                          = "5a783323a6241eb1aba9915ec17102d364493fb3a949af1cbffd33d69753b410"
    image                                       = "sha256:0a399eb16751829e1af26fea27b20c3ec28d7ab1fb72182879dcae1cca21206a"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "ExampleNginxContainer"
    network_data                                = [
        {
            gateway                   = "172.17.0.1"
            global_ipv6_address       = [90mnull[0m[0m
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.2"
            ip_prefix_length          = 16
            ipv6_gateway              = [90mnull[0m[0m
            mac_address               = "02:42:ac:11:00:02"
            network_name              = "bridge"
        },
    ]
    network_mode                                = "bridge"
    pid_mode                                    = [90mnull[0m[0m
    privileged                                  = false
    publish_all_ports                           = false
    read_only                                   = false
    remove_volumes                              = true
    restart                                     = "no"
    rm                                          = false
    runtime                                     = "runc"
    security_opts                               = []
    shm_size                                    = 64
    start                                       = true
    stdin_open                                  = false
    stop_signal                                 = "SIGQUIT"
    stop_timeout                                = 0
    tty                                         = false
    user                                        = [90mnull[0m[0m
    userns_mode                                 = [90mnull[0m[0m
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = [90mnull[0m[0m

    ports {
        external = 8080
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

### Terraform outputs

```shell
terraform output
                           
container_id = "5a783323a6241eb1aba9915ec17102d364493fb3a949af1cbffd33d69753b410"
image_id = "sha256:0a399eb16751829e1af26fea27b20c3ec28d7ab1fb72182879dcae1cca21206anginx:latest"
```

## GitHub

### Terraform import

```shell
terraform import "github_repository.terraform" "devops-terraform"

var.github_token
  Specifies the GitHub PAT token or `GITHUB_TOKEN`

  Enter a value: 

github_repository.terraform: Importing from ID "S25-core-course-labs"...
github_repository.terraform: Import prepared!
  Prepared github_repository for import
github_repository.terraform: Refreshing state... [id=S25-core-course-labs]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
```

### Outputs

```shell
terraform state show github_repository.terraform
terraform state list
terraform output
```

These outputs will give you details about infrastructure and applied changes.
