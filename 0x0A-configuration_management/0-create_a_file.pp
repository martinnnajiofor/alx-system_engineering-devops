file {'/tmp/school':
  ensure  => 'present', 
  replace => 'no',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
