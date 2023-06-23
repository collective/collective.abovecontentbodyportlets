from plone.app.layout.viewlets.common import ViewletBase
from zope.component import getMultiAdapter


class AboveContentBodyPortletsViewlet(ViewletBase):
    # Taken over from plone.app.portlets.browser.viewlets.
    # See there for why a viewlet is needed: basically we need the right context.

    def render_portlets(self):
        portlet_manager = getMultiAdapter(
            (self.context, self.request, self.__parent__),
            name="collective.abovecontentbodyportlets",
        )
        portlet_manager.update()
        return portlet_manager.render()
