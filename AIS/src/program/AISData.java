package program;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.apache.commons.lang3.StringUtils;

/**
 *
 * @author kizilkaya.c3411
 */
public class AISData {

	static Map<String, String> aisMap;
	static Map<String, String> kineticMap;
	static Map<String, String> myCharMap;

	static {
		aisMap = new HashMap<>();
		kineticMap = new HashMap<>();
		myCharMap = new HashMap<>();
	}

	public static void main(String[] args) throws FileNotFoundException, IOException {

		File file = new File("C:\\tmp\\11Sep19.txt");

		BufferedReader br = new BufferedReader(new FileReader(file));
		String st;
		while ((st = br.readLine()) != null) {
			if (st.startsWith("ais")) {
				st += ";";
			}
			int startIndex = StringUtils.ordinalIndexOf(st, ";", 2) + 1;
			int endIndex = StringUtils.ordinalIndexOf(st, ";", 4);

			String key = st.substring(startIndex, endIndex);

			if (StringUtils.isEmpty(key)) {
				continue;
			}

			if (st.startsWith("ais")) {

				if (aisMap.get(key) != null) {
					continue;
				}

				aisMap.put(key, st);
			} else if (st.startsWith("kin")) {

				String aisStr = aisMap.get(key);

				if (StringUtils.isEmpty(aisStr)) {
					continue;
				}

				int aisDateStartIndex = StringUtils.ordinalIndexOf(aisStr, ";", 1) + 1;
				int aisDateEndIndex = StringUtils.ordinalIndexOf(aisStr, ";", 2);
				String aisDate = aisStr.substring(aisDateStartIndex, aisDateEndIndex);

				// aisStr tarihi ile st 'deki tarih aynı olmalı !
				int kinDateStartIndex = StringUtils.ordinalIndexOf(st, ";", 1) + 1;
				int kinDateEndIndex = StringUtils.ordinalIndexOf(st, ";", 2);
				String kinDate = st.substring(kinDateStartIndex, kinDateEndIndex);

				if (aisDate.equals(kinDate)) {
					kineticMap.put(key, st);
				}

			} else if (st.startsWith("cha")) {

				String aisStr = aisMap.get(key);

				if (StringUtils.isEmpty(aisStr)) {
					continue;
				}

				int aisDateStartIndex = StringUtils.ordinalIndexOf(aisStr, ";", 1) + 1;
				int aisDateEndIndex = StringUtils.ordinalIndexOf(aisStr, ";", 2);
				String aisDate = aisStr.substring(aisDateStartIndex, aisDateEndIndex);

				int charDateStartIndex = StringUtils.ordinalIndexOf(st, ";", 1) + 1;
				int charDateEndIndex = StringUtils.ordinalIndexOf(st, ";", 2);
				String charDate = st.substring(charDateStartIndex, charDateEndIndex);

				if (aisDate.equals(charDate)) {
					myCharMap.put(key, st);
				}
			}
		}

		System.out.println("aisMap.size() : " + aisMap.size());
		System.out.println("kineticMap.size() : " + kineticMap.size());
		System.out.println("myCharMap.size() : " + myCharMap.size());

		if (aisMap.values().isEmpty()) {
			// System.out.println("AIS BULUNAMADI !");
			br.close();
			return;
		}

		List<AisKineticChar> targetModels = new ArrayList<>();

		aisMap.keySet().forEach(k -> {

			String ais = aisMap.get(k);

			String kinetic = kineticMap.get(k);
			if (StringUtils.isEmpty(kinetic)) {
				return;
			}

			String myChar = myCharMap.get(k);
			if (StringUtils.isEmpty(myChar)) {
				return;
			}

			AisKineticChar aisKineticChar = new AisKineticChar(k, ais, kinetic, myChar);
			targetModels.add(aisKineticChar);
		});

		System.out.println("targetModels size : " + targetModels.size());

		List<String> fileOutputList = new ArrayList<>();

		targetModels.forEach(testModel -> {
			// System.out.println(testModel.toString());

			String testAis = testModel.getAis();
			testAis = testAis.concat(";X"); // Splitte sorun cıkmasın diye en sonra X ekledik
			// List<String> aisFieldList = Arrays.asList(testAis.split(";"));

			StringBuilder finalString = new StringBuilder();
			finalString.append(testModel.getAis());

			String testKinetic = testModel.getKinetic();
			testKinetic = testKinetic.concat(";X"); // Splitte sorun cıkmasın diye en sonra X ekledik
			List<String> kineticFieldList = Arrays.asList(testKinetic.split(";"));

			// System.out.println("Kinetic: " + testKinetic);
			for (int i = 0; i < kineticFieldList.size(); i++) {
				// System.out.println((i + 1) + " . " + kineticFieldList.get(i));

				if (i > 3 && kineticFieldList.size() != (i + 1)) {
					finalString.append(kineticFieldList.get(i)).append(";");
				}
				if (i == 4) {
					double d = Double.parseDouble(kineticFieldList.get(i));
					if (d < 25 || d > 45) {
						System.out.println("Hatalı veri, bulundu:" + d + "," + kineticFieldList.get(i));
					}
				}
			}
			String testMyChar = testModel.getMyChar();
			testMyChar = testMyChar.concat(";X"); // Splitte sorun cıkmasın diye en sonra X ekledik
			List<String> myCharFieldList = Arrays.asList(testMyChar.split(";"));

			// System.out.println("Kinetic: " + testMyChar);
			for (int i = 0; i < myCharFieldList.size(); i++) {
				// System.out.println((i + 1) + " . " + myCharFieldList.get(i));

				if (i > 3 && myCharFieldList.size() != (i + 1)) {
					finalString.append(myCharFieldList.get(i)).append(";");
				}
			}

			// Sondaki olmaması gereken ';' çıkarılır
			String outputStr = finalString.substring(0, finalString.length() - 1);
			fileOutputList.add(outputStr);

		});

		FileWriter writer = new FileWriter("C:\\tmp\\11Sep19_output.txt");
		for (String str : fileOutputList) {
			writer.write(str + System.lineSeparator());
		}
		writer.close();
		br.close();

	}

}
