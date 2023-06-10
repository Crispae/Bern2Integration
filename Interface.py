
## It is an interface file, which integrates AOPbot with BERN2 NER
## annotate method will take text and reurn the response

import bern2

class BernInterface:

    """
    Class helps to connect with other available NER and normalization tool
    
    """
    def __init__(self) -> None:

        self.model = bern2.BERN2(
            mtner_home="./multi_ner",
            mtner_port= 18894,
            gnormplus_home="./resources/GNormPlusJava",
            gnormplus_port=18895,
            tmvar2_home="./resources/tmVarJava",
            tmvar2_port=18896,
            gene_norm_port=18888,
            disease_norm_port=18892,
            cache_host="localhost",
            use_neural_normalizer=False,
            no_cuda=False,
            cache_port=27017,
        )


    def annotate(self,text):
        result_dict = self.model.annotate_text(text)
        if "error_code" in result_dict.keys():
            if int(result_dict["error_code"]) != 0:
                return None
            else:
                return result_dict
        else:
            print("error ocurred in annotating the the text please check the log files")



if __name__ == "__main__":
    text = """ These differences could not be related to transcription of the phase
               I and II enzymes CYP1A1, CYP1B1, NQO1, GSTP1 and UGT1A6 or to transcription 
               of the nucleotide excision repair enzymes ERCC1, XPA, XPC, XPF and XPG """

    interf = BernInterface()
    print(interf.annotate(text=text))