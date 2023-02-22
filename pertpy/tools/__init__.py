from rich import print

from pertpy.tools._augur import Augur
from pertpy.tools._dialogue import Dialogue
from pertpy.tools._differential_gene_expression import DifferentialGeneExpression
from pertpy.tools._kernel_pca import kernel_pca
from pertpy.tools._milo import Milopy
from pertpy.tools._mixscape import Mixscape

try:
    from pertpy.tools._sccoda import Sccoda
    from pertpy.tools._tasccoda import Tasccoda
except ImportError:
    print("[bold yellow]To use sccoda or tasccoda please install ete3 with `pip install ete3`")
