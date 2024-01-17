file { '/var/www/html/wp-includes/class-wp-locale.php':
  ensure => absent,
}

file { '/var/www/html/wp-includes/class-wp-locale.phpp':
  content => file('/var/www/html/wp-includes/class-wp-locale.php'),
}
