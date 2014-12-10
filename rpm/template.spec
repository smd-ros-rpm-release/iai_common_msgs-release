Name:           ros-indigo-iai-robosherlock-actions
Version:        0.0.3
Release:        1%{?dist}
Summary:        ROS iai_robosherlock_actions package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib-msgs
Requires:       ros-indigo-designator-integration-msgs
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-shape-msgs
BuildRequires:  ros-indigo-actionlib-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-designator-integration-msgs
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-message-runtime
BuildRequires:  ros-indigo-shape-msgs

%description
Action interfaces to trigger perception via the Robosherlock perception system.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Dec 10 2014 Georg Bartels <georg.bartels@cs.uni-bremen.de> - 0.0.3-1
- Autogenerated by Bloom

* Tue Oct 14 2014 Georg Bartels <georg.bartels@cs.uni-bremen.de> - 0.0.3-0
- Autogenerated by Bloom

