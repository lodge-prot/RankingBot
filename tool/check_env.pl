#!/usr/bin/env perl

use warnings;
use strict;
no warnings 'once';
use Sys::Hostname;

#use DateTime;

sub exec_command {
    print "===== Yum Package Install Check =====\n";
    my @exec_command = ('docker', 'docker-compose', 'pip');
    push @exec_command, @_;

    foreach(@exec_command) {
        if (system("which " . $_ . "> /dev/null 2>&1")) {
            warn "[FAILED] Not Installed : $_";
        } else {
            s/ version//;
            printf "[OK] : $_\n";
        }
    }

}

sub check_installed {
    my $item = shift;
    my $packages = shift;

    foreach(@$packages) {
        return 0 if $_ eq $item;
    }
    return 1;
}

sub get_pip_list{
    print "===== Pip Package Install Check =====\n";
    my @res_buf;
    my $file_path = $_[0];
    my @installed_package_list;

    # 現状インストールされているパッケージを取得
    my $command = "pip3 list";
    open my $rs, "$command 2>&1 |";
    my @rlist = <$rs>;
    close $rs;
    foreach(@rlist) {
        if (/Package|----/) {
            next;
        }
        s/ .*$//;
        push @installed_package_list, $_;
    }

    # 要求されているパッケージのリストが入っているか確認
    open(FH, "< $file_path") or die("error :$!");
    while (<FH>) {
        s/=.*$//;
        if (check_installed $_, \@installed_package_list) {
            #print "[FAILED] : $_";
            push @res_buf, "[FAILED] : $_";
        } else {
            #print "[OK] : $_";
            push @res_buf, "[OK] : $_";
        }
    }
    foreach(reverse sort @res_buf) {
        print $_;
    }
}

sub main {
    print "===== Base Info =====\n";
    print "EXEC DATE    : $^T\n";
    print "OS           : $^O\n";
    my $host = hostname();
    print "HOSTNAME     : ", $host, "\n";
    my $ipaddr_bin = gethostbyname($host);
    my @ipaddr_arr = unpack("C4",$ipaddr_bin);
    my $ipaddr_str = sprintf("%u.%u.%u.%u",@ipaddr_arr);
    print "IP Addr      : $ipaddr_str\n";
    print "Perl version : $^V\n";


    exec_command @_;
    get_pip_list "../rankingbot/requirements.txt";
    exit(0);
}

main(@ARGV);
