from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer

import collective.abovecontentbodyportlets


class CollectiveAboveContentBodyPortletsLayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=collective.abovecontentbodyportlets)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "collective.abovecontentbodyportlets:default")


COLLECTIVE_ABOVE_CONTENT_PORTLETS_FIXTURE = CollectiveAboveContentBodyPortletsLayer()


COLLECTIVE_ABOVE_CONTENT_PORTLETS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_ABOVE_CONTENT_PORTLETS_FIXTURE,),
    name="CollectiveAboveContentBodyPortletsLayer:IntegrationTesting",
)


COLLECTIVE_ABOVE_CONTENT_PORTLETS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_ABOVE_CONTENT_PORTLETS_FIXTURE,),
    name="CollectiveAboveContentBodyPortletsLayer:FunctionalTesting",
)
