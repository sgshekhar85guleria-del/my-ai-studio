class SelfImprover:

    def improve(self, prompt, response, score):

        # अगर response weak है तो सुधार करो
        if score < 3:
            improved = f"Improved Answer:\n{response}\n\n(Enhanced explanation added)"
            return improved, True

        return response, False