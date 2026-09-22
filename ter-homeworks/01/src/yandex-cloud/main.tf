terraform {
  required_providers {
    yandex = {
      source  = "yandex-cloud/yandex"
      version = "0.228.0"
    }
  }

  required_version = "~>1.16.0"
}

provider "yandex" {
  token     = var.yc_token
  cloud_id  = var.yc_cloud_id
  folder_id = var.yc_folder_id
  zone      = var.yc_zone
}

resource "yandex_compute_instance" "vm" {
  name        = "docker-vm"
  platform_id = "standard-v3"
  zone        = var.yc_zone

  resources {
    cores         = 2
    core_fraction = 20
    memory        = 1
  }

  scheduling_policy {
    preemptible = true
  }

  boot_disk {
    disk_id = yandex_compute_disk.boot-disk.id
  }

  network_interface {
    subnet_id = data.yandex_vpc_subnet.default.id
    nat       = true
  }

  metadata = {
    ssh-keys = "${var.ssh_user}:${file(var.ssh_public_key_path)}"
  }
}

data "yandex_compute_image" "ubuntu" {
  family = "ubuntu-2404-lts-oslogin"
}

resource "yandex_compute_disk" "boot-disk" {
  name     = "docker-vm-boot"
  type     = "network-hdd"
  size     = 10
  zone     = var.yc_zone
  image_id = data.yandex_compute_image.ubuntu.id
}

data "yandex_vpc_subnet" "default" {
  name = "default-${var.yc_zone}"
}
