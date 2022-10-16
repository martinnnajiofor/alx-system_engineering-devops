file_line {'set PasswordAuthentication to no':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}

file_line {'use school as private key auth':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
}
