ACLOCAL_AMFLAGS=-I m4

SUBDIRS = inc

data_sdidir= $(sysconfdir)/opx/sdi
data_sdi_DATA = cfg/sdi/*.sql 

#The sdi-sys library
lib_LTLIBRARIES = libopx_sdi_db.la

libopx_sdi_db_la_SOURCES = src/sdi_db_ops.c
libopx_sdi_db_la_CPPFLAGS = -I$(top_srcdir)/inc/opx -I$(includedir)/opx -I$(top_srcdir)/inc/opx/private
libopx_sdi_db_la_LDFLAGS = -version-info 1:1:0
libopx_sdi_db_la_LIBADD = -lopx_db_sql

lib_LTLIBRARIES += libopx_sdi_sys.la

libopx_sdi_sys_la_SOURCES = \
	src/sdi_db_ops.c \
	src/sdi_vm_entity.c \
	src/sdi_vm_fan.c \
	src/sdi_vm_led.c \
	src/sdi_vm_media.c \
	src/sdi_vm_nvram.c \
	src/sdi_vm_sys.c \
	src/sdi_vm_thermal.c

libopx_sdi_sys_la_CPPFLAGS = -I$(top_srcdir)/inc/opx  -I$(includedir)/opx  -I$(top_srcdir)/inc/opx/private
libopx_sdi_sys_la_LDFLAGS = -version-info 1:1:0
libopx_sdi_sys_la_LIBADD = libopx_sdi_db.la -lopx_db_sql -lopx_logging -lpthread -lrt
