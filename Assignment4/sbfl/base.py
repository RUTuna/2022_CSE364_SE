import sbfl_formula
import pandas as pd

# TODO: Implement fault localization
class SBFL:
    def __init__(self, formula='Ochiai'):
        self.formula = formula
        self.totalfailed = 0
        self.totalpassed = 0
        self.line_SBFL = pd.DataFrame(columns=['"file"','"line"','"passed"','"failed"','"totalpassed"','"totalfailed"','"score"','"rank"'])
        self.func_SBFL = pd.DataFrame(columns=['"score"','"rank"'])
    
    def cal_formula(self, e_p, n_p, e_f, n_f):
        if self.formula == 'Jaccard':
            return sbfl_formula.Jaccard(e_p, n_p, e_f, n_f)
        elif self.formula == 'Tarantula':
            return sbfl_formula.Tarantula(e_p, n_p, e_f, n_f)
        else:
            return sbfl_formula.Ochiai(e_p, n_p, e_f, n_f)


    def cal_line_score(self, cov_df, failing_tests):
        total_results = []
        for index, row in cov_df.iterrows():
            e_p = 0
            e_f = 0

            for fail in failing_tests:
                if row[fail] : # failing_test 중 커버한 횟수 확인
                    e_f = e_f + 1


            for covered in row:
                if covered:
                    e_p = e_p + 1 # 모든 테스트 케이스 중 해당 라인 커버한 횟수
            
            e_p = e_p - e_f # fail 제외해서 pase 만 두게
        
            score = self.cal_formula(e_p, self.totalpassed, e_f, self.totalfailed)
            filename = index[0][index[0].rfind('/') + 1:]
            result = [filename, index[2], e_p, e_f, self.totalpassed, self.totalfailed, score, 0] # 결과 생성
            total_results.append(result)
        
        self.line_SBFL = pd.DataFrame(total_results, columns=['"file"','"line"','"passed"','"failed"','"totalpassed"','"totalfailed"','"score"','"rank"'])
        self.line_SBFL = self.line_SBFL.sort_values(by=['"score"'])



    def cal_func_score(self, cov_df, failing_tests):
        total_results = []
        funcs = {}
        for index, row in cov_df.iterrows():
            if type(index[1]) is float: # 함수명 NaN 제거
                continue
            func_name = index[1]
            file_name = index[0][index[0].rfind('/') + 1:]
            funcs[func_name] = file_name # 함수 이름 저장 딕셔너리 key: func_name, value: file_name
            
            e_p = 0
            e_f = 0

            for fail in failing_tests:
                if row[fail] : # failing_test 중 커버한 횟수 확인
                    e_f = e_f + 1


            for covered in row:
                if covered:
                    e_p = e_p + 1 # 모든 테스트 케이스 중 해당 라인 커버한 횟수
            
            e_p = e_p - e_f # fail 제외해서 pase 만 두게

            score = self.cal_formula(e_p, self.totalpassed, e_f, self.totalfailed)
            df_index = [(file_name, func_name)]
            result = [score, 0, index[2]] # 결과 생성
            if df_index[0] in self.func_SBFL.index: # df 내에 존재
                if self.func_SBFL.at[df_index[0], '"score"'] < score:
                    self.func_SBFL.at[df_index[0]] = result
            else :
                df = pd.DataFrame([result], index = pd.MultiIndex.from_tuples(df_index, names=['"file"', '"function"']), columns=['"score"','"rank"', '"line"'])
                if self.func_SBFL.empty:
                    self.func_SBFL = df
                else:
                    self.func_SBFL = self.func_SBFL.append(df)
        
        self.func_SBFL = self.func_SBFL.sort_values(by=['"score"'])

    # 함수별로 count하는 코드
        # total_results = []
        # funcs = {}
        # e_p = {}
        # e_f = {}
        # for index, row in cov_df.iterrows():
        #     func_name = index[1]
        #     if func_name not in e_p:
        #         e_p[func_name] = 0
        #     if func_name not in e_f:
        #         e_f[func_name] = 0

        #     for covered in row:
        #         funcs[index[1]] = index[0][index[0].index('//') + 2:] # 함수 이름 저장 딕셔너리 key: func_name, value: file_name
        #         if covered:
        #             e_p[index[1]] = e_p[index[1]] + 1

            
        #     for fail in failing_tests:
        #         if row[fail] : # failing_test 중 커버한 횟수 확인
        #             e_f[index[1]] = e_f[index[1]] + 1

        
        # for func_name, file_name in funcs.items():
        #     score = self.cal_formula(e_p[func_name] - e_f[func_name], self.totalpassed, e_f[func_name], self.totalfailed)
        #     result = [file_name, func_name, score, 0] # 결과 생성
        #     total_results.append(result)
        
        # self.func_SBFL = pd.DataFrame(total_results, columns=['file','function','score','rank'])
        # self.func_SBFL = self.func_SBFL.sort_values(by=['score'])
        # print(self.func_SBFL)
