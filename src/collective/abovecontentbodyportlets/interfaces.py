from plone.app.portlets.interfaces import IColumn
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ICollectiveAboveContentBodyPortletsLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IPortletColumn(IColumn):
    """Our portlet provider."""
