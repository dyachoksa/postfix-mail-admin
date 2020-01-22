<?php
namespace Deployer;

require 'recipe/common.php';
require 'recipe/rsync.php';

// Project name
set('application', 'postfix_mail_admin');

// Project repository
// set('repository', 'git@github.com:dyachoksa/postfix-mail-admin.git');
set('rsync_src', '.');

// SSH settings
set('ssh_multiplexing', false);

// [Optional] Allocate tty for git clone. Default value is false.
set('git_tty', true);

// Shared files/dirs between deploys
set('shared_files', [".env"]);
set('shared_dirs', []);

// Writable dirs by web server
set('writable_dirs', []);

// Configuring the rsync exclusions.
add('rsync', [
    'exclude' => [
        '.git',
        '/app.db',
        '/.env',
        '/.vagrant/',
        '/.venv/',
        '/node_modules/',
        '/docs/',
        '/assets/',
        '/deploy.php',
    ],
]);


// Hosts

host('postfix-mail.local')
    ->hostname('172.23.81.108')
    ->stage('testing')
    ->user('sergey')
    ->set('deploy_path', '/home/app/{{application}}');


// Tasks

desc('Deploy your project');
task('deploy', [
    'deploy:info',
    'deploy:prepare',
    'deploy:lock',
    'deploy:release',
    'rsync',
    'deploy:shared',
    'deploy:writable',
    'deploy:clear_paths',
    'deploy:symlink',
    'deploy:unlock',
    'cleanup',
    'success'
]);

// [Optional] If deploy fails automatically unlock.
after('deploy:failed', 'deploy:unlock');
