# session.py
#
# Copyright 2025
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation at version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os


def is_kde_session() -> bool:
    """
    Detect if the current session is KDE/Plasma.
    
    Returns:
        bool: True if running in a KDE/Plasma session, False otherwise.
    """
    # Check XDG_CURRENT_DESKTOP environment variable
    xdg_current_desktop = os.environ.get("XDG_CURRENT_DESKTOP", "").lower()
    if "kde" in xdg_current_desktop or "plasma" in xdg_current_desktop:
        return True
    
    # Check XDG_SESSION_DESKTOP environment variable as fallback
    xdg_session_desktop = os.environ.get("XDG_SESSION_DESKTOP", "").lower()
    if "kde" in xdg_session_desktop or "plasma" in xdg_session_desktop:
        return True
    
    return False


def get_session_specific_file(base_filename: str, moduledir: str) -> str:
    """
    Get the session-specific version of a file if it exists, otherwise return the base file.
    
    For example, if base_filename is "apps.json" and we're in a KDE session,
    this will return the path to "apps-kde.json" if it exists, otherwise "apps.json".
    
    Args:
        base_filename: The base filename (e.g., "apps.json")
        moduledir: The module directory path
    
    Returns:
        str: The full path to the session-specific file or the base file
    """
    if is_kde_session():
        # Extract name and extension
        name, ext = os.path.splitext(base_filename)
        kde_filename = f"{name}-kde{ext}"
        kde_path = os.path.join(moduledir, kde_filename)
        
        # Return KDE-specific file if it exists, otherwise fall back to base file
        if os.path.exists(kde_path):
            return kde_path
    
    # Return the base file path
    return os.path.join(moduledir, base_filename)


def get_session_specific_path(base_path: str) -> str:
    """
    Get the session-specific version of a file path if it exists, otherwise return the base path.
    
    For example, if base_path is "/etc/snow/images.json" and we're in a KDE session,
    this will return "/etc/snow/images-kde.json" if it exists, otherwise "/etc/snow/images.json".
    
    Args:
        base_path: The full path to the base file
    
    Returns:
        str: The full path to the session-specific file or the base file
    """
    if is_kde_session():
        # Extract directory, name and extension
        dirname = os.path.dirname(base_path)
        basename = os.path.basename(base_path)
        name, ext = os.path.splitext(basename)
        kde_path = os.path.join(dirname, f"{name}-kde{ext}")
        
        # Return KDE-specific file if it exists, otherwise fall back to base file
        if os.path.exists(kde_path):
            return kde_path
    
    return base_path
