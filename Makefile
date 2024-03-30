install:
	mkdir -p /usr/share/device_gui
	cp -r rootfs/* /
	cp -r ./* /usr/share/device_gui
	chmod +x /usr/share/device_gui/scripts/*
	chmod +x /usr/share/device_gui/run.sh

	systemctl daemon-reload
	systemctl enable gui.service