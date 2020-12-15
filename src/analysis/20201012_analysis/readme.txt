# 2020/12/07  

- 処理の説明  
  - 02_make_data_20201012_exp_r02_prefit.ipynb  
  - 10/12取得データに対して、r02メソッドで視点を再計算し保存するスクリプト(車体外壁が人の前に位置しておりおかしな値が出るため再計算が必要)  
  - 保存先：2020_moox_morikoro_project/preprocess_data/20201012_preprocess_data/pkl/02_20201012_preprocess_data.pkl

  - 03_make_fig_20201015_exp_r02_nofit_output.ipynb  
  - 再計算結果を作図し、外周補正を行っていない状況の精度を評価するスクリプト  
  - 作図保存先　：2020_moox_morikoro_project/output/20201012_output_data/fig/20201012_preprocess_data/03_20201012_exp_section_prefix/*.png  
  - 統計量保存先：2020_moox_morikoro_project/output/20201012_output_data/st_data/20201012_preprocess_data/03_20201012_exp_section_prefix/*.csv  

  - 04_make_fig_20201015_exp_r02_fit_output.ipynb  
  - 10/12取得データに手動でアノテーションを行い、解析形式に変換し保存するスクリプト  
  - 作図保存先　：2020_moox_morikoro_project/output/20201012_output_data/fig/20201012_preprocess_data/04_20201012_exp_section_fix_1/*.png  
  - 統計量保存先：2020_moox_morikoro_project/output/20201012_output_data/st_data/20201012_preprocess_data/04_20201012_exp_section_fix_1/*.csv  
